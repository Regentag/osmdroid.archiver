# osmdroid.archiver
Generate SQLite Tile Archive (Offline Map) for Osmdroid-android

# 개요
[Osmdroid-android](https://github.com/osmdroid/osmdroid)를 위한 SQLite3 형식의 Archive를 생성합니다.

Python 버전 : 3

# 사용법
    python arc.py [Tile Dir] [Provider] [Archive Name]

* Tile Dir : 별도의 GIS 도구를 사용하여 생성한 Tile 이미지가 저장된 디렉터리입니다. Zoom Level의 상위 디렉터리까지 지정합니다.
 * 다음과 같은 구조를 가집니다.

    ./TileDir
        (Provider)
            (Zoom Level)
                (X)
                    (Y.jpg)
            ...
            ...

* Provider : Map Provider. ex) Mapnik
* Archive Name : 생성될 archive 파일명.

## 예시
다음과 같이 Tile 이미지가 저장된 경우 Tile Dir는 `./KorPeninsula/Mapnik` 입니다.

    ./KorPeninsula
        - Mapnik
            - 0
                - 1
                    - 1.jpg
                    - 2.jpg
                - 2
                    - 1.jpg
                    - 2.jpg
            - 1
                - 1
                    - 1.jpg
                    - 2.jpg
            ...
            ...

명령:

    python arc.py ./KorPeninsula/Mapnik Mapnik KorPeninsula.sqlite

# 참조
Osmdroid의 Offline Map Tiles에 대한 설명은 다음 문서를 참조하십시오.
https://github.com/osmdroid/osmdroid/wiki/Offline-Map-Tiles

SQLite3 형식 Archive의 구조는 `org.osmdroid.tileprovider.modules.DatabaseFileArchive` 클래스의 코드를 참조하십시오.
https://github.com/osmdroid/osmdroid/blob/master/osmdroid-android/src/main/java/org/osmdroid/tileprovider/modules/DatabaseFileArchive.java

Osmdroid에서 사용되는 Tile System에 대한 설명은 Microsoft Bing Map의 Tile System 설명을 참조하십시오.
https://msdn.microsoft.com/ko-kr/library/bb259689.aspx
