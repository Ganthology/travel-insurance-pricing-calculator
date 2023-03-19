from  typing import Optional

def calculate_insurance_price(period_days: int, plan: int):
    price = 0
    match plan:
        case 1:
            # 1 - 5 Days: $43
            # 6 - 10 Days: $70
            # 11 - 18 Days: $107
            # 19 - 31 Days: $126
            # 32+ Days: $126 + $34 per week
            if period_days > 31:
                extra_weeks = (period_days - 31) // 7
                price = 126 + extra_weeks * 34
            elif period_days > 19:
                price = 126
            elif period_days > 10:
                price = 107
            elif period_days > 5:
                price = 70
            else:
                price = 43
        case 2:
            # 1 - 5 Days: $65
            # 6 - 10 Days: $105
            # 11 - 18 Days: $161
            # 19 - 31 Days: $189
            # 32+ Days: $189 + $50 per week
            if period_days > 31:
                extra_weeks = (period_days - 31) // 7
                price = 189 + extra_weeks * 50
            elif period_days > 19:
                price = 189
            elif period_days > 10:
                price = 161
            elif period_days > 5:
                price = 105
            else:
                price = 65
        case 3:
            # 1 - 5 Days: $75
            # 6 - 10 Days: $122
            # 11 - 18 Days: $187
            # 19 - 31 Days: $216
            # 32+ Days: $216 + $59 per week
            if period_days > 31:
                extra_weeks = (period_days - 31) // 7
                price  = 216 + extra_weeks * 59
            elif period_days > 19:
                price = 216
            elif period_days > 10:
                price = 187
            elif period_days > 5:
                price = 122
            else:
                price = 75
        case _:
            raise ValueError("Invalid plan")

    return price
         
def calculate_covid_addon_price(period_days: int, plan: int):
    price = 0
    match plan:
        case 1:
            # 1 - 5 Days: $23
            # 6 - 10 Days: $33
            # 11 - 18 Days: $54
            # 19 - 31 Days: $85
            # 32+ Days: $126 + $34 per week
            if period_days > 31:
                extra_weeks = (period_days - 31) // 7
                price = 126 + extra_weeks * 34
            elif period_days > 19:
                price = 126
            elif period_days > 10:
                price = 107
            elif period_days > 5:
                price = 70
            else:
                price = 43
        case 2:
            # 1 - 5 Days: $36
            # 6 - 10 Days: $50
            # 11 - 18 Days: $78
            # 19 - 31 Days: $120
            # 32+ Days: $120 + $35 per week
            if period_days > 31:
                extra_weeks = (period_days - 31) // 7
                price = 120 + extra_weeks * 35
            elif period_days > 19:
                price = 120
            elif period_days > 10:
                price = 78
            elif period_days > 5:
                price = 50
            else:
                price = 36
        case 3:
            # 1 - 5 Days: $59
            # 6 - 10 Days: $79
            # 11 - 18 Days: $118
            # 19 - 31 Days: $117
            # 32+ Days: $117 + $56 per week
            if period_days > 31:
                extra_weeks = (period_days - 31) // 7
                price = 117 + extra_weeks * 56
            elif period_days > 19:
                price = 117
            elif period_days > 10:
                price = 118
            elif period_days > 5:
                price = 79
            else:
                price = 59
        case _:
            raise ValueError("Invalid plan")

    return price