import logging

logging.basicConfig(
    level=logging.INFO,
    format=(
        '%(asctime)s - %(name)s - %(levelname)s'
        ' %(filename)s:%(lineno)d - %(message)s'
    ),
    datefmt='%Y-%m-%dT%H:%M:%S',
)

log = logging.getLogger('app')
log.info('Loading data')
