import json
import logging
import os

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# The Slack web hook url
slack_hook_url = os.environ['slack_hook_url']
# The Slack channel
slack_channel = os.environ['slack_channel']
# Alarm when severity higher than setting
alarm_severity = os.environ['alarm_severity']
region = os.environ['AWS_DEFAULT_REGION']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    detail = event['detail']
    logger.info("Detail: " + str(detail))

    severity = detail['severity']
    logger.info("severity: " + str(severity))
    title = detail['title']
    logger.info("title: " + str(title))
    description = detail['description']
    logger.info("description: " + str(description))

    if float(severity)>=float(alarm_severity):

      finding_url = "https://" + region + ".console.aws.amazon.com/guardduty/home?region=" + region + "#/findings?macros=current&fId=" + detail['id']
      
      slack_message = {
        "channel" : slack_channel,
        "text" : "Guard Alarm Severity: %s\nTitle: %s\nDetails: %s\nFinding: %s" % (severity,title,description,finding_url)
      }
      req = Request(slack_hook_url, json.dumps(slack_message).encode('utf-8'))
      try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
      except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
      except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
    else:
      logger.info("Current alarm severity is %s", ALARM_SEVERITY)