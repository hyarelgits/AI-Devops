For your first AIOps/RAG project, you don't need hundreds of runbooks.

Start with 10-15 practical runbooks.

Your current folders are:

Plain Text



docs/
├── agents
├── incidents
├── linux
├── network
├── runbooks
└── security


Inside runbooks/, I recommend:

db-recovery.txt
server-restart.txt
cpu-high.txt
memory-high.txt
disk-full.txt
postgres-down.txt
apache-down.txt
nginx-down.txt
docker-service-down.txt
network-connectivity.txt
dns-issue.txt
filesystem-full.txt
vm-performance.txt
backup-restore.txt
user-access-issue.txt



Priority Order

Create these first:

1. cpu-high.txt

Issue: High CPU Usage

Resolution:
1. Run top
2. Find high CPU process
3. Check logs
4. Restart service



========


memory-high.txt

Issue: High Memory Usage

Resolution:
1. Run free -h
2. Check memory-consuming process
3. Restart application

===================


disk-full.txt


Issue: Disk Space Full

Resolution:
1. Run df -h
2. Find large files
3. Remove unnecessary files



===============



postgres-down.txt


Issue: PostgreSQL Service Down

Resolution:
1. systemctl status postgresql
2. Check logs
3. Restart service




=============


network-connectivity.txt


Issue: Network Not Reachable

Resolution:
1. ping gateway
2. Verify routing
3. Check firewall



=================



Why Add More Runbooks?

Right now your AI knows:

Plain Text
Database Recovery

Only.

So:

Plain Text
How do I recover database?

✅ Good answer

But:

Plain Text
Why CPU is high?

❌ Poor answer

After adding multiple runbooks:

Plain Text
Why CPU is high?

↓

Plain Text
Run top
Check PID
Review logs
Restart service
Good Target

For a demo project:

Plain Text
10 runbooks ✅ Good
25 runbooks ✅ Very Good
50+ runbooks ✅ Production-like

My recommendation:

Plain Text
Create 10 runbooks first
Re-ingest them
Test RAG
Then move to the next phase:
Prometheus Alert → PostgreSQL Incident → AI Analysis

Since you already have:

Plain Text
db-recovery.txt
server-restart.txt

the next files I'd create are:

Plain Text
cpu-high.txt
memory-high.txt
disk-full.txt
postgres-down.txt
network-connectivity.txt
 

These 5 give the biggest improvement to your AI assistant. 🚀








