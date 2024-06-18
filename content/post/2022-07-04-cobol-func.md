---
layout: post
title:  "GNUCobol语言函数"
date: 2022-07-04 15:12:54
categories: [编程语言,cobol]
tags: [cobol, linux]
excerpt_separator: <!--more-->
---
GNUCobol语言函数
<!--more-->

## 自定义函数

```cobol
       IDENTIFICATION DIVISION.
       FUNCTION-ID. F-GOLD.
       DATA DIVISION.
       LINKAGE SECTION.
       01 NUM_IN PIC 9(10).
       01 NUM_OUT PIC 9(10).
       PROCEDURE DIVISION USING BY VALUE NUM_IN RETURNING NUM_OUT.
       BEGIN.
           COMPUTE NUM_OUT = - (NUM_IN + 1).
       END FUNCTION F-GOLD.   
       IDENTIFICATION DIVISION.

      ******************************************************************
       PROGRAM-ID. SAMPLE.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       REPOSITORY.
           FUNCTION F-GOLD.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 WS-Count-NUM PIC 9(03) VALUES 10.
       01 WS-Param-NUM PIC 9(10) 
           OCCURS 10 TIMES
           INDEXED BY WS-P-IDX.
       77 N-SUCCESS PIC 9(03).
       PROCEDURE DIVISION.
       BEGIN.

           MOVE 20 TO WS-Param-NUM(1).
           MOVE 68 TO WS-Param-NUM(2).
           MOVE 52 TO WS-Param-NUM(3).
           MOVE 61 TO WS-Param-NUM(4).
           MOVE 03 TO WS-Param-NUM(5).
           MOVE 88 TO WS-Param-NUM(6).
           MOVE 41 TO WS-Param-NUM(7).
           MOVE 78 TO WS-Param-NUM(8).
           MOVE 94 TO WS-Param-NUM(9).
           MOVE 18 TO WS-Param-NUM(10).
           
           MOVE 0 TO N-SUCCESS.

           PERFORM VARYING WS-P-IDX FROM 1 BY 1 
               UNTIL WS-P-IDX > WS-Count-NUM
               IF 
                   FUNCTION F-GOLD(WS-Param-NUM(WS-P-IDX)) = 
                   FUNCTION F-GOLD(WS-Param-NUM(WS-P-IDX)) THEN
                   ADD 1 TO N-SUCCESS
               END-IF
           END-PERFORM.
           DISPLAY "#Results: " N-SUCCESS ", " WS-Count-NUM.
           STOP RUN.
       END PROGRAM SAMPLE.
```
output
```bash
#Results: 010, 010
```

## 系统函数

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. SAMPLE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 NUM-Count PIC S9(3)V9(3) VALUES +10.
       PROCEDURE DIVISION.
       BEGIN.
           DISPLAY NUM-Count.
           MOVE -10 TO NUM-Count.
           DISPLAY NUM-Count.
           DISPLAY FUNCTION ABS(NUM-Count).
           MOVE FUNCTION ABS(NUM-Count) TO NUM-Count.
           DISPLAY NUM-Count.
           COMPUTE NUM-Count = -1 * NUM-Count.
           DISPLAY NUM-Count.
           STOP RUN.
       END PROGRAM SAMPLE.
```
output
```bash
+010.000
-010.000
+010.000
+010.000
-010.000
```

## 子程序

主程序
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAIN.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           01 WS-STUDENT-ID PIC 9(4) VALUE 1000.
           01 WS-STUDENT-NAME PIC A(15) VALUE 'Tim'.
       
       PROCEDURE DIVISION.
           CALL 'UTIL' USING WS-STUDENT-ID, WS-STUDENT-NAME.
           DISPLAY 'Student Id : ' WS-STUDENT-ID
           DISPLAY 'Student Name : ' WS-STUDENT-NAME
       STOP RUN.
```
子程序
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. UTIL.
       
       DATA DIVISION.
       LINKAGE SECTION.
           01 LS-STUDENT-ID PIC 9(4).
           01 LS-STUDENT-NAME PIC A(15).
       
       PROCEDURE DIVISION USING LS-STUDENT-ID, LS-STUDENT-NAME.
           DISPLAY 'In Called Program'.
           MOVE 1111 TO LS-STUDENT-ID.
       EXIT PROGRAM.
```
output
```bash
In Called Program
Student Id : 1111
Student Name : Tim
```