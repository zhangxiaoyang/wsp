#!/usr/bin/env bash
#-*- coding:utf-8 -*-

# 这个脚本用于启动Master。

bin=`dirname "${BASH_SOURCE-$0}"`
bin=`cd "$bin"; pwd`

$bin/../pyscripts/start-master.py $bin/../etc/master.yaml $bin/../etc/system.yaml
