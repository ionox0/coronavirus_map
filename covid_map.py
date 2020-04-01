import folium
import pandas as pd



def create_map(table, zips, mapped_feature, add_text=''):

	nyc_geo = r'nyc_zipcodes.geojson'
	m = folium.Map(location = [40.7128, -74.0060], zoom_start = 11)

	m.choropleth(
		geo_data = nyc_geo,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		data = table,
		key_on = 'feature.properties.postalCode',
		columns = [zips, mapped_feature],
		fill_color = 'PuBuGn',
		legend_name = (' ').join(mapped_feature.split('_')).title() + ' ' + add_text + ' Across NYC'
	)

	folium.LayerControl().add_to(m)

	m.save(outfile = mapped_feature + '_map.html')


if __name__ == '__main__':
	table = pd.read_csv('covid_positive_by_zip.csv')
	table['MODZCTA'] = table['MODZCTA'].astype(str)
	zips = 'MODZCTA'
	mapped_feature = 'Positive'
	add_text = ''

	create_map(table, zips, mapped_feature)
