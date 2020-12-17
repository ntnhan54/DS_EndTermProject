# KHOA HỌC DỮ LIỆU ỨNG DỤNG
---
**Đồ án cuối kỳ môn Khoa Học Dữ Liệu Ứng Dụng**

 **GV Hướng dẫn: Hoàng Xuân Trường**

## Thành Viên

* Nguyễn Phúc Khôi Nguyên - 1712xxx
* Nguyễn Thành Nhân - 1712631

## Tổng Quan Đồ Án

1. Đặt vấn đề
2. Thu thập dữ liệu
3. Khám phá và tiền xử lí dữ liệu
4. Phân tích dữ liệu $\rightarrow$ Thiết lập mô hình dự đoán
5. Tự đánh giá
6. Phân công
7. Hướng dẫn chạy

### Đặt vấn đề
> Gần đây diễn ra nhiều cuộc thi về âm nhạc, và câu hỏi đặt ra là làm sao để giám khảo có thể biết được chất lượng của bài hát đó thay vì cách nghe và cảm nhận (một cách khá cảm tính) như bình thường.

> Giả sử bạn là một nghệ sĩ và bạn cần một công cụ để đánh giá bài hát của mình đã tốt chưa, có khả quan và có được khán giả hứng thú. Nếu bài hát chưa hay thì chưa hay ở điểm nào và bạn có thể điều chỉnh được không?

**Các công cụ có thể trợ giúp việc đưa ra quyết định cho các giám khảo hoặc ca sĩ. Giúp họ điều chỉnh các thuộc tính của bài hát để có hiệu quả tốt. Ví dụ như ca sĩ nên lựa chọn thời lượng của bài hát là bao nhiêu để có thể thu hút nhiều người yêu thích  hoặc nên ưu tiên phát hành ở khu vực nào để có hiệu quả tốt nhất**

### Thu thập dữ liệu
> * Sử dụng `API` của Spotify, dịch vụ cung cấp âm nhạc kỹ thuật số nổi tiếng.
> * Thu thập danh sách id của các playlist có trên Spotify (Do API cung cấp) và lưu vào `playlist.csv`
> * Thu thập các id của các bài hát có trong danh sách playlist đã thu thập và lưu vào `tracks.txt`
> * Thu thập các id của nghệ sĩ (artists) của các bài hát đã thu thập và các thuộc tính của bài hát đó thông qua id đã thu thập trước đó và lưu vào `tracks.csv` và `feature.csv`
> * Thu thập thông tin của nghệ sĩ thông qua id và lưu vào `artists.csv`

$\rightarrow$ Dữ liệu được thu thập thành các file: `playList.txt`, `tracks.txt`, `tracks.csv`, `artists.csv`, `feature.csv`
### Khám phá và tiền xử lí dữ liệu (EDA)

#### Khám phá dữ liệu
- Merge 2 dataframe feature và tracks thành dataframe cho bài hát `df_track`
- Khám phá trên 2 df: df_track và df_artist
- df_track có 69162 dòng và 23 thuộc tính, df_artist có 24544 dòng và 5 thuộc tính. Trong đó các thuộc tính được mô tả trong bảng sau:
##### Giải thích các cột trong df_track
|STT|Tên cột|Kiểu dữ liệu|Ý nghĩa|
|---|---|---|---|
|0  |artists |string|ID Spotify của các nghệ sĩ trình bày ca khúc, cách nhau bởi dấu "," |
|1  |available_markets   |string|Các khu vực trên thế giới có thể nghe bài hát, mỗi nước là một code 2 chữ in hoa, cách nhau bởi dấu ","|
|2  |explicit            |bool|True nếu bài hát chứa nội dung không phù hợp cho mọi đối tượng, ngược lại là False|
|3  |popularity          |int|Độ yêu thích, từ 0-100|
|4  |danceability        |float|Mức độ phù hợp của bài hát để nhảy, đo từ 0-1|
|5  |energy              |float|Mức độ sôi động của bài hát, đo từ 0-1|
|6  |key                 |int|Tông của bài hát, nếu không xác định, nhận giá trị là -1|
|7  |loudness            |float|Độ lớn db của bài hát từ -60 - 0|
|8  |mode                |int|1 cho biết bài hát viết theo "major", 0 là "minor"|
|9  |speechiness         |float|Từ 0-1, 0 có nghĩa bài hát không có lời, 1 có nghĩa bài hát có phần lời phức tạp|
|10 |acousticness        |float|Từ 0-1, khả năng bài hát có thể trình bày dưới dạng acoustic|
|11 |instrumentalness    |float|Từ 0-1, càng nhỏ cho thấy bài hát có phần lời ít|
|12 |liveness            |float|Từ 0-1, mức độ phù hợp để trình diễn trực tiếp|
|13 |valence             |float|Từ 0-1, mức độ tích cực của nội dung bài hát|
|14 |tempo               |float|Từ 0-1, độ nhanh của nhạc nền (số beat trên 1 phút)|
|15 |type            |string|Kiểu dữ liệu trả về khi gọi api, tất cả đều là "audio features"|
|16 |uri             |string|URI của bài hát|
|17 |track_href      |string|Link tới bài hát|
|18 |analysis_url    |string|Link tới phần đặc trưng âm thanh của bài hát|
|19 |duration_ms     |int|Độ dài bài hát|
|20 |time_signature  |int|Số beat của 1 câu trong bài hát|

##### Giải thích các cột trong df_artist
|STT|Tên cột|Kiểu dữ liệu|Ý nghĩa|
|---|---|---|---|
|0  |followers |int|Số người theo dõi|
|1  |genres   |string|Thể loại theo đuổi, có dạng một list các str|
|2  |name            |string|Tên nghệ sĩ|
|3  |popularity          |int|Độ yêu thích, từ 0-100|

#### Tiền xử lí dữ liệu
<!-- - Xóa các thuộc tính không phải số của df_track, trừ thuộc tính `available_markets` -->
- Xóa các mẫu có giá trị available_markets là null.
- Chia dữ liệu ra thành 3 tập train, develop, test.
### Phân tích dữ liệu -> Thiết lập mô hình dự đoán
- Phân tích tương quan giữa các thuộc tính

    ![Correlation giữa các thuộc tính](./image/track_corr.png)

    $\rightarrow$ Các cặp thuộc tính có tương quan lớn với nhau là (loudness, energy) và (acousticness, energy)
- 



### Tự đánh giá
### Phân công
### Hướng dẫn chạy