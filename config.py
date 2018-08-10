import redis
import logging

class Config(object):
    """工程配置信息"""
    DEBUG = True
    SECRET_KEY = 'jpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Y'

    """数据库相关配置"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:mysql@192.168.31.157:3306/infomation'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """REDIS相关配置"""
    REDIS_HOST = '192.168.31.157'
    REDIS_PORT = '6379'

    """flask session 的配置信息"""
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST)
    PREMANENT_SESSION_LIFETIME = 86400
    LOG_LEVEL = logging.DEBUG

class DevelopmentConfig(Config):
    """开发模式下的配置"""
    pass


class ProductionConfig(Config):
    """生产环境配置"""
    LOG_LEVEL = logging.ERROR



config = {
   "development":DevelopmentConfig,
    "production":ProductionConfig
}