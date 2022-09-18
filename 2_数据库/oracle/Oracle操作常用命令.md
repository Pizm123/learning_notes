1. 实例

   ```shell
   #查看实例
   echo $ORACLE_SID
   #切换实例
   export ORACLE_SID=orcl
   ```

2. 监听

   ```shell
   #查看监听状态
   lsnrctl status
   #停止监听
   lsnrctl stop
   #启动监听
   lsnrctl start
   ```

3. sqlPlus

   ```shell
   # 连接
   sqlplus / as sysdba
   # 停止实例
   shutdown immediate
   # 启动实例
   startup
   ```

4. 导入导出dmp

   ```shell
   # 导出
   exp zxuser/zxuserkcb@172.16.37.132:1521/dribank  file=./ log=./ full=y
   # 导入
   imp stu_db/stu_db@192.168.126.128/orcl file=‪C:\Users\pizm1\Desktop\stu.dmp fromuser=stu_db touser=stu_db
   ```

5. 表空间及用户

   ```sql
   -- 创建表空间
   create tablespace data_test datafile 'e:\oracle\oradata\test\data_1.dbf' size 2048M;
   -- 创建用户
   create user C##stu_db identified by stu_db default tablespace pizmTs temporary tablespace temp;
   -- 授权
   grant connect,resource,dba to stu_db;
   ```

   

