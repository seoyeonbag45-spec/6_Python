from loader import load_prices,load_companies,load_sectors

def load_merged():
    prices = load_prices()
    companies = load_companies()
    sectors = load_sectors().rename(columns={"code":"sectorCode", "name":"sector"})

    df = (
        prices
        .merge(companies[['code','name','sectorCode','market']],
            on='code', how='left',validate='many_to_one')
        .merge(sectors[['sectorCode','sector']],
            on='sectorCode', how='left',validate='many_to_one')

        )
    return df.sort_values(['code', 'date']).reset_index(drop=True)