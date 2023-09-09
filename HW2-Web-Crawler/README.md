# 104 HR 爬蟲程式

此 Python 程式用於爬取 104 人力銀行網站的工作職缺資訊。

## 程式功能

1. 爬取指定關鍵字的工作職缺資訊。
2. 可選擇是否多條件搜尋（地區）。
3. 輸出爬取結果到 CSV 檔案。

## 使用說明

1. 執行程式後，請輸入要搜尋的關鍵字。如果要取消，請輸入 "0"。
2. 然後，您可以選擇是否需要多條件搜尋（地區）。請輸入 "Y" 表示需要，或 "N" 表示不需要。如果要取消，請輸入 "0"。
3. 如果選擇多條件搜尋，請輸入要搜尋的地區。如果要取消，請輸入 "0"。
4. 程式將爬取相應的工作職缺資訊，並將結果輸出到 CSV 檔案中。

## 注意事項

- 程式會自動建立名稱為 "日期-關鍵字 地區-104HR.csv" 的 CSV 檔案，存儲在 "jobs_csv" 資料夾中。
- 如需更改保存路徑或檔案名稱，請編輯程式中的路徑設定。

---


# 104 HR Web Scraper

This Python program is designed to scrape job vacancy information from the 104 Job Bank website.

## Program Features

1. Scrapes job vacancy information for specified keywords.
2. Optionally allows multiple criteria searches (by location).
3. Outputs the scraped results to a CSV file.

## Usage Instructions

1. Upon running the program, please enter the keyword you want to search for. To cancel, type "0."
2. Next, you can choose whether you want to perform a multi-criteria search (by location). Type "Y" for yes or "N" for no. To cancel, type "0."
3. If you choose a multi-criteria search, please enter the location you want to search for. To cancel, type "0."
4. The program will scrape the relevant job vacancy information and output the results to a CSV file.

## Notes

- The program will automatically create a CSV file named "Date-Keyword Location-104HR.csv," stored in the "jobs_csv" folder.
- If you need to change the save path or file name, please edit the path settings in the program.

---

Thank you for using the 104 HR Web Scraper! If you have any questions or need further assistance, please feel free to contact us.
