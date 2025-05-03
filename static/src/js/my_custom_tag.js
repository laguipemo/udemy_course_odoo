odoo.define('real_estate_ads.CustomAction', function (require) {
    'use strict';

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');

    var CustomAction = AbstractAction.extend({
        template: 'CustomActionsTemplate',
        start: function () {
            console.log("Action Log Start")
        }
    });

    core.action_registry.add('custom_client_action', CustomAction);
});