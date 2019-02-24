import logging
from celery import shared_task

from fb_wall.users.models import User

logger = logging.getLogger(__name__)


@shared_task
def send_welcome_email(user_id):
    try:
        user = User.objects.get(pk=user_id)

        user_merge_data = {
            user.email: {
                '%first_name%': user.first_name,

            }
        }
        user.send_template_email("cda2b867-9e4b-40bc-a84a-1fe1daafb752", user_merge_data)

    except User.DoesNotExist:
        logger.info("Cannot send welcome email, cannot find user <ID %s>" % str(user_id))
