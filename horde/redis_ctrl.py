import socket
import redis

hostname = "localhost"
port = 6379
address = f"redis://{hostname}:{port}"

limiter_db = 1
ipaddr_db = 2
cache_db = 3
ipaddr_supicion_db = 4
ipaddr_timeout_db = 5

horde_users_db = 10
horde_workers_db = 11
horde_teams_db = 12
horde_stats_db = 16

def is_redis_up() -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((hostname, port)) == 0

def ger_limiter_url():
    return(f"{address}/{limiter_db}")

def ger_cache_url():
    return(f"{address}/{cache_db}")

def get_ipaddr_db():
    rdb = redis.Redis(
        host=hostname,
        port=port,
        db = ipaddr_db)
    return(rdb)

def get_ipaddr_suspicion_db():
    rdb = redis.Redis(
        host=hostname,
        port=port,
        db = ipaddr_supicion_db)
    return(rdb)

def get_ipaddr_timeout_db():
    rdb = redis.Redis(
        host=hostname,
        port=port,
        db = ipaddr_timeout_db)
    return(rdb)


def get_horde_dbs():
    users_db = redis.Redis(
        host=hostname,
        port=port,
        db = horde_users_db)
    workers_db = redis.Redis(
        host=hostname,
        port=port,
        db = horde_workers_db)
    teams_db = redis.Redis(
        host=hostname,
        port=port,
        db = horde_teams_db)
    stats_db = redis.Redis(
        host=hostname,
        port=port,
        db = horde_stats_db)
    return(users_db,workers_db,teams_db,stats_db)
