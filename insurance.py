command to run insuranc  crew :
#######in celerary: run as admin ########
conda activate insurance
(insurance) D:\Insurance\Motor_Insurance_AI_Agent_Test_Instance\motor_policy>
celery -A celery_app worker --pool=threads --concurrency=3 -l info
########in redis :run ad admin#########
cd C:\Program Files\Redis
redis-server.exe
########frontend#######
cd
npm run dev
########backend########
uvicorn run_api:app --reload
