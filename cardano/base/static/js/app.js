$(document).ready(function() {
    'use strict';

    var countries = new Array();
    $('tr.country-block').each(function(i, obj) {
        countries.push(obj);
    });

    $('[data-toggle="tooltip"]').tooltip();

    var t = $('#filterCountries');
    t.bind('propertychange keyup input paste', function(event) {
        var term = t.val().toLowerCase();
        if (term !== '') {
            $('.country-block').hide();
            var results = $.grep(countries, function(e) {
                if ($(e).data('selector').indexOf(term) !== -1) {
                    return $(e);
                }
            });
            $(results).show();
        } else {
            $('.country-block').show();
        }
    });
});
