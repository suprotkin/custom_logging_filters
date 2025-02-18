from pythonjsonlogger import json

class JsonFormatter(json.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        log_record['level'] = record.levelname
        log_record['timestamp'] = self.formatTime(record, self.datefmt)
        log_record['logger'] = record.name
