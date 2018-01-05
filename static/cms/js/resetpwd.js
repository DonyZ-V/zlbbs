/**
 * Created by Administrator on 2018/1/3.
 */

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();
        var oldpwdE = $('input[name=oldpwd]');
        var newpwdE = $('input[name=newpwd]');
        var newpwd2E = $('input[name=newpwd2]');

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        //1. 要在模板的meta标签中渲染一个crsf-token
        //2. 在ajax请求的头部中设置X-CRSFtoken
        zlajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('恭喜！密码修改成功！');
                    oldpwdE.val('');
                    newpwdE.val('');
                    newpwd2E.val('');
                } else {
                    var message = data['message'];
                    zlalert.alertInfo(message)
                }

            },
            'fail': function (error) {
                zlalert.alertNetworkError()
            }
        })
    })
});
