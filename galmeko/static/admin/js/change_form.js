/*global showAddAnotherPopup, showRelatedObjectLookupPopup showRelatedObjectPopup updateRelatedObjectLinks*/

(function($) {
    'use strict';
    $(document).ready(function() {
        var modelName = $('#django-admin-form-add-constants').data('modelName');
        $('body').on('click', '.add-another', function(e) {
            e.preventDefault();
            var event = $.Event('django:add-another-related');
            $(this).trigger(event);
            if (!event.isDefaultPrevented()) {
                showAddAnotherPopup(this);
            }
        });

        if (modelName) {
            $('form#' + modelName + '_form :input:visible:enabled:first').focus();
        }
    });

       //User Add Form Js

       var type = $("#id_type").val();
       if (type == 1) {
           $('.dynamic-title').text('Add Hospital');
       }
       $("#id_type").on('change', function (e) {
           var type = $("#id_type").val();
           if (type == 1) {
   
           } else if (type == 2) {
               $('#hospital-group').css('display', 'none');
               $('.dynamic-title').text('Add Vendor');
           }
       });
})(django.jQuery);
