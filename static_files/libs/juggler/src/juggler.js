(function (window) {
    'use strict';

    function juggle() {
        for (var name in window.Juggler.registry) {
            if (!window.Juggler.registry.hasOwnProperty(name)) {
                continue;
            }

            var entry = window.Juggler.registry[name];
            var matchedTarget = null;

            // Find the matching target
            for (var i = 0; i < entry.targets.length; i++) {
                var target = entry.targets[i];

                // Media query matches, break the loop as media query has a priority
                if ((target.mediaQuery !== null && window.matchMedia(target.mediaQuery).matches)) {
                    matchedTarget = target;
                    break;
                }

                // Flag matches
                if ((target.flag !== null && window.Juggler.getFlag(target.flag))) {
                    matchedTarget = target;
                }
            }

            // Move the element to the matched target
            if (matchedTarget !== null) {
                // Only move it if it's not already there
                if (matchedTarget.comment !== entry.location) {
                    matchedTarget.comment.parentNode.insertBefore(entry.sourceElement, matchedTarget.comment.nextSibling);
                    entry.location = entry.comment;
                }

                continue;
            }

            // Move the element from target to source, but only if it's not already there
            if (entry.location !== entry.sourceComment) {
                entry.sourceComment.parentNode.insertBefore(entry.sourceElement, entry.sourceComment.nextSibling);
                entry.location = entry.sourceComment;
            }
        }
    }

    window.Juggler = window.Juggler || {
        /**
         * Custom flags
         */
        flags: {},

        /**
         * Element registry
         */
        registry: {},

        /**
         * Initialize the Juggler
         * @returns {void}
         */
        init: function () {
            Array.prototype.slice.call(document.querySelectorAll('[data-juggler-target]')).forEach(function (targetElement) {
                var target = targetElement.dataset.jugglerTarget;
                var sourceElements = document.querySelectorAll('[data-juggler-source="' + target + '"]');

                // Throw an error if the source element has been not found
                if (sourceElements.length === 0) {
                    throw new Error('The element source "' + target + '" does not exist.');
                }

                // Throw an error if the number of source elements is bigger than one
                if (sourceElements.length > 1) {
                    throw new Error('The element source "' + target + '" is not unique. ' + sourceElements.length + ' elements have been found.');
                }

                var sourceElement = sourceElements[0];
                var sourceComment = document.createComment('Juggler source: ' + target);
                var comment = document.createComment('Juggler target: ' + target);

                // Create the registry entry if it does not exist yet
                if (!this.registry.hasOwnProperty(target)) {
                    this.registry[target] = {
                        location: sourceComment,
                        sourceElement: sourceElement,
                        sourceComment: sourceComment,
                        targets: []
                    };

                    // Prepend the source comment to element
                    sourceElement.parentNode.insertBefore(sourceComment, sourceElement);
                }

                this.registry[target].targets.push({
                    comment: comment,
                    mediaQuery: targetElement.dataset.jugglerMediaQuery || null,
                    flag: targetElement.dataset.jugglerFlag || null
                });

                // Replace the element with target comment
                targetElement.parentNode.replaceChild(comment, targetElement);
            }.bind(this));

            window.addEventListener('resize', juggle);
            juggle();
        },

        /**
         * Set the flag value
         * @param {String} name Flag name
         * @param {Boolean} value Flag value (true or false)
         * @returns {void}
         */
        setFlag: function (name, value) {
            this.flags[name] = !!value;
            juggle();
        },

        /**
         * Get the flag value
         * @param {String} name Flag name
         * @returns {Boolean} Flag value (true or false)
         */
        getFlag: function (name) {
            if (!this.flags.hasOwnProperty(name)) {
                return false;
            }

            return this.flags[name];
        }
    };
}(window));
