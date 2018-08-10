from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import pymysql
import redis
from flask_wtf.csrf import CSRFProtect
from config import config
import logging



db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    """传入不同参数，初始化不同配置"""
    """配置项目日志"""
    setup_log(config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    CSRFProtect(app)
    Session(app)
    """注册蓝图"""
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)
    return app


def setup_log(config_name):
    """配置日志"""
    logging.basicConfig(level=config[config_name].LOG_LEVEL)
    file_log_hander = RotatingFileHandler("logs/log",maxBytes=1024 * 1024 * 100,backupCount=10)
    formatter = logging.Formatter('%(levername)s %(filename)s:%(lineno)d %(message)s')
    file_log_hander.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_hander)




