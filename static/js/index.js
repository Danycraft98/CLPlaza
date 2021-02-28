function set_required() {
    $(":input[name='value']").prop('required', function () {
        return $(this).is(':visible');
    });
}


function load_ajax(container, details, return_func) {
    const url = details.url, method = details.request;
    $(function () {
        $.ajax({
            url: url, method: method,
            async: true, crossDomain: true,
            //credentials: 'include',
            headers: {
                'cache-control': 'no-cache',
                'postman-token': 'e044290e-4cb5-3056-fbc3-de2c26cecb79',
            },
            beforeSend: function () {
                $(container).html('Loading...');
            },
            fail: resp => console.log(resp, method, url)
        }).done(function (resp) {
            return_func(resp, url, method);
        });
    });
}


function formatML(node, level) {
    let indentBefore = new Array(level++ + 1).join('    '),
        indentAfter = new Array(level - 1).join('    '),
        textNode;

    if (!node.children) return node;
    Array.from(node.children).forEach(function (child) {
        textNode = document.createTextNode('\n' + indentBefore);
        node.insertBefore(textNode, child);
        formatML(child, level);

        if (node.lastElementChild === child) {
            textNode = document.createTextNode('\n' + indentAfter);
            node.appendChild(textNode);
        }
    })
    return node;
}


function write_result(respText, url, method) {
    if (!respText) result_div.text('None');
    const result_div = $('#result'), html = document.createElement('html');
    html.innerHTML = respText.trim();
    $('#url').text(method + ' ' + url);
    result_div.text(formatML(html, 0).outerHTML);
}


function getMethods(obj) {
    let properties = new Set()
    let currentObj = obj
    do {
        Object.getOwnPropertyNames(currentObj).map(item => properties.add(item))
    } while ((currentObj = Object.getPrototypeOf(currentObj)))
    return [...properties.keys()].filter(item => typeof obj[item] === 'function')
}