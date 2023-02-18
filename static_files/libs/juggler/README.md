# Juggler.js

Juggler is a simple tool that allows to move (not copy!) the element nodes from one place to another
in the DOM when they match the provided media query.

## Why?

During the design implementation it can happen that some elements must be moved around as not everything
can be achieved with pure CSS. Consider the following HTML structure:

```html
<div class="header">
    <div class="logo">...</div>
    <div class="navigation">...</div>
    <div class="mobile-box-trigger">...</div>
    <div class="mobile-box">
        <!-- we want to display .navigation here but only on mobile -->
    </div>
</div>
```

What if you had to move the `.navigation` div into the `.mobile-box` but only on the small devices?
That's where the Juggle.js comes in handy and solves the problem with ease:

```html
<div class="header">
    <div class="logo">...</div>
    <div class="navigation" data-juggler-source="navigation">...</div>
    <div class="mobile-box-trigger">...</div>
    <div class="mobile-box">
        <!-- the .navigation will be displayed here on mobile -->
        <div data-juggler-target="navigation" data-juggler-media-query="(max-width: 767px)"></div>
    </div>
</div>
```

## How it works?

When the document is ready (e.g. `DOMContentLoaded` event is triggered) the script gathers all Juggler elements
and puts them in an internal registry. To preserve the location of the source and target elements for further
reference the HTML comments are added before the source element and as a replacement of the target element.
This way the temporary placeholders do not interfere with other elements and do not break CSS nor JS.

## Installation

Download the package and include the file on your page:

```html
<script src="assets/js/juggler.min.js"></script>
```

Then intiialize the script once DOM is ready:

```js
document.addEventListener('DOMContentLoaded', Juggler.init());

// or

document.addEventListener('DOMContentLoaded', function () {
    Juggler.init();
});
```

## Configuration

There are basically two things you have to configure:

1. **Source element**

The original element you would like to juggle. It must have a unique ID specified the attribute:

```html
<div data-juggler-source="my_unique_id">...</div>
```

2. **Target element**

The element that will be replaced by the source element when necessary. It must refer to the existing source element
and contain a valid [CSS media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries):

```html
<div data-juggler-target="my_unique_id" data-juggler-media-query="(max-width: 767px)"></div>
```

### Using boolean flags instead of media queries

You can also use the boolean flags instead of media queries, see the demo files for example.

```html
<div data-juggler-source="my_unique_id">...</div>
<div data-juggler-target="my_unique_id" data-juggler-flag="foobar"></div>

<script>
Juggler.setFlag('foobar', true);
Juggler.setFlag('foobar', false);
</script>
```

## Known issues

1. When you clone an element that is a Juggler source, make sure to remove the data attribute or you will get
an error of duplicate source items.

## Copyright

This project has been created and is maintained by [Codefog](https://codefog.pl).
