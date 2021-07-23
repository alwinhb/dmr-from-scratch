# from dmrpy.fixtures.symbol_stream import (
#     EXAMPLE_SYMBOL_STREAM_SHORT,
# )
# from dmrpy.layer_1.symbol_stream_to_packets import symbol_stream_to_packets

# EXPECTED_SYMBOL_STREAM_SHORT = [
#     ("cach", 4091713),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810348880354553664891390444590284454430,
#     ),
#     ("cach", 11977059),
#     (
#         "traffic",
#         9184171478469433557825732916299397226784850773072409542289177174013219678560555,
#     ),
#     ("cach", 665514),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810016573355607435923164492825214368286,
#     ),
#     ("cach", 10618387),
#     (
#         "traffic",
#         935175765838861082135966784351515153256211642475432258484373886808809131828835,
#     ),
#     ("cach", 4095809),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810016573355607435923164492825214368286,
#     ),
#     ("cach", 11977059),
#     (
#         "traffic",
#         4895349440850397948306386103759992427519188198882844495984439382838654086028067,
#     ),
#     ("cach", 665258),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368725278288624319049025546792732342401566,
#     ),
#     ("cach", 10618387),
#     (
#         "traffic",
#         3054263395412787668918079522119991761544587948245388123744781598939667308308683,
#     ),
#     ("cach", 4095809),
#     (
#         "traffic",
#         28879701874005529008463106180551436074281697730641595360789299264990292552235550,
#     ),
#     ("cach", 11977059),
#     (
#         "traffic",
#         3524840354312763889370824309886481803523706698622533032963354409621078452872844,
#     ),
#     ("cach", 665514),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810016573355607435923164492825214368286,
#     ),
#     ("cach", 10618387),
#     (
#         "traffic",
#         5010673044713061596948121720945335532774183825221617936348179113799810273764256,
#     ),
#     ("cach", 4095809),
#     (
#         "traffic",
#         28879701874005529008463106180551436074281697730641595360789299264990292552235550,
#     ),
#     ("cach", 11977059),
#     (
#         "traffic",
#         8730961072591210587809171491867371298125607308110792933431931844695653575744400,
#     ),
#     ("cach", 665258),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368725278288624319049025546792732342401566,
#     ),
#     ("cach", 10618387),
#     (
#         "traffic",
#         6739706760855307634784575893372787603206584872323227389783943923680365800353768,
#     ),
#     ("cach", 4095809),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810016573355607435923164492825214368286,
#     ),
#     ("cach", 11977059),
#     (
#         "traffic",
#         1767087796355922276071690291394954409633335568360333295877229566690786638635036,
#     ),
#     ("cach", 665514),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810016573355607435923164492825214368286,
#     ),
#     ("cach", 10618387),
#     (
#         "traffic",
#         1433801372926027203416693135663718842409386649365892842358134778485118107911300,
#     ),
#     ("cach", 4095809),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368724945981625372820057320840967272315422,
#     ),
#     ("cach", 11977059),
#     (
#         "traffic",
#         11880683247764389301232982680700122727124647435631040256855546993748492803731004,
#     ),
#     ("cach", 665514),
#     (
#         "traffic",
#         28879701874005528905619071347976058439596123820726059160953700981195762087803422,
#     ),
#     ("cach", 10618387),
#     (
#         "traffic",
#         4240380004239582752764902219036578010093941003127058012061754950508847288921012,
#     ),
#     ("cach", 4091713),
#     (
#         "traffic",
#         28879701874005476300895254485670398298012096488155261590790829471187734457268766,
#     ),
#     ("cach", 11977059),
#     (
#         "traffic",
#         734126672445760972620295820966503669815210188236235838816883197279712166128396,
#     ),
#     ("cach", 665258),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368725278288624319049025546792732342401566,
#     ),
#     ("cach", 10618387),
#     (
#         "traffic",
#         6183653284108122475643435108282897918228749403165767241037791025100087039362836,
#     ),
#     ("cach", 4095809),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810016573355607435923164492825214368286,
#     ),
#     ("cach", 11977059),
#     (
#         "traffic",
#         21350270377458585685498026939496065484342348557127048393477505644412232745761564,
#     ),
#     ("cach", 665514),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810016573355607435923164492825214368286,
#     ),
#     ("cach", 10618387),
#     (
#         "traffic",
#         9457832579596765971099284795132259772945612489309941342195117088879332983494168,
#     ),
#     ("cach", 4095809),
#     (
#         "traffic",
#         28879701874005529008463106180551436074368810016573355607435923164492825214368286,
#     ),
#     ("cach", 11977059),
# ]


# def test_symbol_stream_to_packets_symbol_stream_short():
#     assert (
#         list(symbol_stream_to_packets(EXAMPLE_SYMBOL_STREAM_SHORT))
#         == EXPECTED_SYMBOL_STREAM_SHORT
#     )


# def test_symbol_stream_to_packets_list_of_ones():
#     assert list(symbol_stream_to_packets([1] * 10000)) == list()


# def test_symbol_stream_to_packets_list_of_noise():
#     assert list(symbol_stream_to_packets([1, -3, 1, 3, 3, -1] * 10000)) == list()
