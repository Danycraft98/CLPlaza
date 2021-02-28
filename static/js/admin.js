$(document).ready(function () {
    // Formatting all the admin site to look aesthetically pleasing
    $('#content-main').addClass('card container-fluid py-4 mb-4')
        .find('select').parent().addClass('form-inline');
    $("table:not('.table')").addClass('table table-border')
    $('#changelist-search div,.actions').addClass('form-inline mb-2 col-6 input-group');

    // Form attributes
    $('.form-row').removeClass('form-row');
    $(":input:not('[type=checkbox],[type=radio]')").addClass('form-control');
    $('label').removeClass('required');

    // Submit Button Category
    $('.submit-row').addClass('btn-group')
        .last().attr('hidden', '');
    $("[value*='Save']").addClass('btn btn-outline-primary');

    const select = $("li[class='selected']").parent(),
        options = select.children();
    if (options) options.replaceWith($('<option>' + $(this).html() + '</option>'));
    select.replaceWith($("<select class='form-select'>" + select.html() + "</select>"));
    $('addlink').attr('hidden', '');
    // console.log($('object-tools'))

    // ----------------------------------------------------------------------

    const link = $("a[id*='add_id']"),
        iframe = $(document.createElement('iframe'));
    link.attr('target', '_blank');
    // link.attr('target', 'foreign');
    iframe.attr('name', 'foreign').attr('class', 'row').attr('style', 'min-height: 0;');

    $(document.createElement('div')).attr('class', 'form-inline')
        .append(iframe)
        .insertAfter(link.parent().parent());
});