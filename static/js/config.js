var require = {
    urlArgs: "v=2.1",
    // RequireJS 通过一个相对的路径 baseUrl来加载所有代码。baseUrl通常被设置成data-main属性指定脚本的同级目录。
    baseUrl: "/static/js/",
    paths: {
        jquery: "lib/jquery/jquery",
        bsAlert: "utils/bsAlert",
        csrfToken: "utils/csrfToken",
        validator: "lib/validator/validator",
    },
};
