class FooTask(Task):
    def run(self, arg1):
        # do stuff
        try:
            ...
        except:
            ...
        else:
            return ret_arg
            

class MarkRunningTask(Task):
    
    def run(self, uuid):

        try:
            session = Session.objects.get(uuid=uuid)

            try:
                session.run()

            except Exception as e:

                raise self.retry(
                    max_retries=settings.MARK_RUNNING_MAX_RETRIES,
                    countdown=settings.MARK_RUNNING_BACKOFF_SECONDS)

            else:
                return session

        except MaxRetriesExceededError:
            logger.error(
                "MarkRunningTask for Session {0} reached "
                "max_retries and was failed.".format(uuid))