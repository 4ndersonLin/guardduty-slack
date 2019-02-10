# GuardDuty Slack

# Deployment
- lambda: upload python to lambda(py 3.6)
- cloudwatch event: setting guardduty trigger lambda

# Environment
```
# The Slack web hook url
slack_hook_url = os.environ['slack_hook_url']
# The Slack channel
slack_channel = os.environ['slack_channel']
# Alarm when severity higher than setting
alarm_severity = os.environ['alarm_severity']
```
