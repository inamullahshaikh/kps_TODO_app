class Status:
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

    VALID_STATUSES = [TO_DO, IN_PROGRESS, COMPLETED]

    def __init__(self, status=TO_DO):
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status! Must be one of {self.VALID_STATUSES}")
        self._status = status

    @property
    def status(self):
        return self._status

    def update_status(self, new_status):
        if new_status in self.VALID_STATUSES:
            self._status = new_status
        else:
            raise ValueError(f"Invalid status! Must be one of {self.VALID_STATUSES}")

    def __str__(self):
        return f"Status: {self._status}"
