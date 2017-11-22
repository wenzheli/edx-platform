define([
    'jquery', 'underscore', 'backbone', 'js/views/utils/xblock_utils', 'js/utils/templates',
    'js/views/modals/course_outline_modals'],
    function(
        $, _, Backbone, XBlockViewUtils, TemplateUtils, CourseOutlineModalsFactory
    ) {
        'use strict';
        var CourseHighlightsEnableView = Backbone.View.extend({
            events: {
                'click button.status-highlights-enabled-value': 'handleEnableButtonPress',
                'keypress button.status-highlights-enabled-value': 'handleEnableButtonPress'
            },

            initialize: function() {
                this.template = TemplateUtils.loadTemplate('course-highlights-enable');
            },

            handleEnableButtonPress: function(event) {
                if (event.type === 'click' || event.key === 'Enter' || event.key === ' ') {
                    event.preventDefault();
                    this.highlightsEnableXBlock();
                }
            },

            highlightsEnableXBlock: function() {
                var modal = CourseOutlineModalsFactory.getModal('highlights_enable', this.model, {
                    onSave: this.refresh.bind(this),
                    xblockType: XBlockViewUtils.getXBlockType(
                        this.model.get('category')
                    )
                });

                if (modal) {
                    window.analytics.track('edx.bi.highlights_enable.modal_open');
                    modal.show();
                }
            },

            refresh: function() {
                this.model.fetch({
                    success: this.render.bind(this)
                });
            },

            render: function() {
                this.$el.html(this.template(this.model.attributes));
                return this;
            }
        });

        return CourseHighlightsEnableView;
    }
);
