print("Стоимость пирожка:")
rubliki = int(input("Рублики:"))
kopeechki = int(input("Копеечки:"))
skoka_pirozhkov = int(input("Сколько пирожков:"))
price = rubliki * 100 + kopeechki
summa = price * skoka_pirozhkov
price_rubliki = summa // 100
price_kopeechki = summa % 100
print("К оплате:" ,price_rubliki,"руб.",price_kopeechki,"коп.",)