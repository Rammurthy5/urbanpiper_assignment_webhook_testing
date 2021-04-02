import datetime 
from apscheduler.schedulers.background import BackgroundScheduler
from api.models import UniqueidTable, DataTable
import logging
import atexit

logger = logging.getLogger(__name__)

sched = BackgroundScheduler(daemon=True)
sched.start()

def cleanup(uniqueid, runtime):
    logger.info("Current List of jobs in the schedule {}".format(sched.print_jobs()))
    sched.add_job(deactivate_endpoints, 'date', run_date=runtime, args=[uniqueid])


def deactivate_endpoints(uniqueid):
    delete_result = UniqueidTable.objects.filter(uniqueid=uniqueid).delete()
    logger.info("Delete result for unique id {} {}".format(uniqueid, delete_result))


@atexit.register
def scheduler_shutdown():
    sched.shutdown()