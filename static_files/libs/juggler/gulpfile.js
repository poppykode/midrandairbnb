'use strict';

const eslint = require('gulp-eslint');
const gulp = require('gulp');
const rename = require('gulp-rename');
const sourcemaps = require('gulp-sourcemaps');
const uglify = require('gulp-uglify');

gulp.task('eslint', function () {
    return gulp.src(['src/juggler.js'])
        .pipe(eslint())
        .pipe(eslint.format())
        .pipe(eslint.failAfterError());
});

gulp.task('default', function () {
    return gulp.src('src/juggler.js')
        .pipe(sourcemaps.init({loadMaps: true}))
        .pipe(rename({dirname: ''}))
        .pipe(gulp.dest('dist'))
        .pipe(uglify())
        .pipe(rename({extname: '.min.js'}))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest('dist'));
});
