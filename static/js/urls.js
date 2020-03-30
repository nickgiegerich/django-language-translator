

    // view the task
    $(".alphabet-modal").each(function () {
        console.log('anything');
        $(this).modalForm({formURL: $(this).data('id')});
    });

