from api.resources.auth import SignupApi, LoginApi

def init_auth_routes(api):
  api.add_resource(SignupApi, '/api/v1/auth/signup')
  api.add_resource(LoginApi, '/api/v1/auth/login')