from flask import Blueprint,request
from exts import alidayu
from utils import restful
from utils.captcha import Captcha
from .forms import SMSCaptchaForm

bp = Blueprint('common',__name__,url_prefix='/c')

@bp.route('/sms_captcha/',methods=['POST'])
def sms_captcha():
    # telephone = request.args.get('telephone')
    # if not telephone:
    #     return restful.params_error(message='请传入手机号码！')
    #
    # captcha = Captcha.gene_text(number=4)
    # if alidayu.send_sms(telephone,code=captcha):
    #     return restful.success()
    # else:
    #     return restful.params_error(message='短信发送失败!')


    #telephone
    #timestamp
    #md5(ts+telephone+salt)
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        if alidayu.send_sms(telephone,code=captcha)
            return restful.success()
        else:
            return restful.params_error()
    else:
        return restful.params_error('参数错误！')

