#!/usr/bin/env bash
# Runs both Front and API Flask servers (Not for production)
(trap 'kill 0' SIGINT; python3 -m web_dynamic.front & python3 -m api.v1.app)
