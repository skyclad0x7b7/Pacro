## Script

이 문서는 Pacro 스크립트 작성방법에 대해 설명합니다.  
This document explains about writing scripts for Pacro.  

문서는 한국어나 영어로 기술합니다.  
The documents should be written in Korean or English.  

Pacro 스크립트는 JSON 형태로 저장되며 모든 명령어는 필수 키로 "id"와 "op"를 갖습니다.  
"op"의 종류에 따라 "arg"는 있을 수도, 없을 수도 있습니다.  
"id"는 스크립트마다 하나씩만 가지는 고유한 값으로 중복될 수 없으며 가능한 0부터 1씩 증가하며 오름차순으로 작성합니다.  
특별한 상황이 아닌 이상 스크립트는 위에서부터 순서대로 실행됩니다.  

id는 부호 없는 정수형이며 op는 문자열입니다.  
arg는 개수에 관계없이 항상 dict형을 유지합니다.  

예시
```
[
    {
        "arg": {
            "x-pos": 100,
            "y-pos": 100
        },
        "id": 0,
        "op": "click"
    },
    {
        "arg": {
            "ms": 1000
        },
        "id": 1,
        "op": "sleep"
    }
]
```


사용 가능할 예정인 op와 그에 따른 arg 리스트.  


### sleep

지정한 시간동안 아무 것도 하지 않고 기다립니다.

인자  
1. ms (필수) : 정수형. 밀리세컨드 단위로 기다릴 시간을 지정합니다.

```
{
    "op":"sleep",
    "arg": {
        "ms" : 100,
    }
}
```

### click

지정한 위치를 클릭합니다.

인자  
1. x-pos (필수) : 부호 없는 정수형. x좌표의 값을 나타냅니다.  
2. y-pos (필수) : 부호 없는 정수형. y좌표의 값을 나타냅니다.  
3. delay (옵션) : 부호 없는 정수형. 누른 후 뗄때까지의 시간을 ms 단위로 지정합니다. 없을 경우 딜레이 없이 진행됩니다.  

```
{
    "op":"click",
    "arg": {
        "x-pos" : 100,
        "y-pos" : 100,
        "delay" : 50
    }
}
```