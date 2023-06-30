
from flask import Blueprint
from flask import jsonify

from datas.metrics import Test, Test_schema

repos_bp = Blueprint('repos', __name__)

@repos_bp.route('/')
def list():
    return jsonify({
        'owner':'kubernetes',
        'repo':'kubernetes',
        'lang':'go'
        })


@repos_bp.route('/test')
def remote_test():
    test = Test.query.all()
    return Test_schema.dump(test)


@repos_bp.route('/sloc')
def sloc():
    test = Test.query.all()
    return Test_schema.dump(test)