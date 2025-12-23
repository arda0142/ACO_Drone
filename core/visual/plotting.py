import pydeck as pdk
import pandas as pd
import matplotlib.pyplot as plt

def harita_ciz(en_iyi_rota, koordinatlar, lokasyon_isimleri):
    path_data = []
    for idx in en_iyi_rota:
        lat, lng = koordinatlar[idx]
        path_data.append([lng, lat])
    start_idx = en_iyi_rota[0]
    path_data.append([koordinatlar[start_idx][1], koordinatlar[start_idx][0]])

    route_points_df = pd.DataFrame([
        {"lat": koordinatlar[idx][0], "lon": koordinatlar[idx][1], "name": lokasyon_isimleri[idx], "order": str(i + 1)}
        for i, idx in enumerate(en_iyi_rota)
    ])
    
    # Katmanlar (Senin büyük yazılı versiyon)
    layer_path = pdk.Layer("PathLayer", data=[{"path": path_data}], get_color=[230, 0, 0], width_scale=20, width_min_pixels=3, get_path="path", get_width=6)
    layer_points = pdk.Layer("ScatterplotLayer", data=route_points_df, get_position='[lon, lat]', get_color=[0, 100, 255], get_radius=200, pickable=True)
    layer_names = pdk.Layer("TextLayer", data=route_points_df, get_position='[lon, lat]', get_text='name', get_color=[0, 0, 0], get_size=19, get_alignment_baseline="'top'", get_pixel_offset=[0, 22])

    view_state = pdk.ViewState(latitude=37.77, longitude=30.55, zoom=12.5)
    
    deck = pdk.Deck(layers=[layer_path, layer_points, layer_names], initial_view_state=view_state, map_style="mapbox://styles/mapbox/light-v9")
    deck.to_html("drone_route_map.html")
    print("Harita oluşturuldu: drone_route_map.html")
