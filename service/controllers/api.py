from flask import Blueprint, abort, render_template

blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/update')
def notify():
    # Verify that it's github or localhost

    # Return forbidden if not verified

    # Return 204 if successful
    pass


@blueprint.route('/rebuild')
def rebuild():
    print('wtf')
    return "HAHA"


"""
def verify_request(payload, ip):

    # Check for secure token

    # Get sha string
    #ver, signature = request.headers.get('X-Hub-Signature')
    if ver != 'sha1':
        abort(501)

    mac = hmac.new(str(secret), msg=request.data, digestmod=sha1)

    if hmac.compare_digest(str(mac.hexdigest()), str(signature))
        return True

    abort(403)
    return False
"""
# TODO: Implement 418 (I'm a teapot)