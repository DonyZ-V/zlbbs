from flask import Blueprint, request, make_response,jsonify
from exts import alidayu
from utils import restful, zlcache
from utils.captcha import Captcha
from .forms import SMSCaptchaForm
from io import BytesIO
import qiniu

bp = Blueprint('common', __name__, url_prefix='/c')


@bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        if alidayu.send_sms(telephone, code=captcha):
            zlcache.set(telephone, captcha)
            return restful.success()
        else:
            return restful.params_error(message='发送失败！')
    else:
        return restful.params_error('参数错误！')


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    zlcache.set(text.lower(), text.lower())
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


@bp.route('/uptoken/')
def uptoken():
    access_key = 'Ph0xk5XcAAfvlZyRSlp-o9TgweYEFwP1pf81LfbU'
    secret_key = 'hBVxy1LWYoiN3K-FLO166nrUboSArouadoBwHjHs'
    q = qiniu.Auth(access_key, secret_key)

    bucket = 'dzbbs'
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})
