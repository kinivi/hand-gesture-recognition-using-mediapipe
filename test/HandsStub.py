from src.domain.Hands import Hands, Hand, Knuckle, Chirality


def should_create_hands():
    return Hands([should_create_hand()])


def should_create_hand() -> Hand:
    return Hand(should_return_knuckles_for_open_hand(), Chirality.RIGHT)


def should_return_knuckles_for_open_hand() -> list[Knuckle]:
    return [
        Knuckle(x=0.7650785446166992, y=0.7659584283828735, z=0.7659584283828735),
        Knuckle(x=0.6762756109237671, y=0.7552127838134766, z=0.7552127838134766),
        Knuckle(x=0.595783531665802, y=0.6722360849380493, z=0.6722360849380493),
        Knuckle(x=0.537173867225647, y=0.5972177386283875, z=0.5972177386283875),
        Knuckle(x=0.48265814781188965, y=0.5525830984115601, z=0.5525830984115601),
        Knuckle(x=0.6476624011993408, y=0.4710245132446289, z=0.4710245132446289),
        Knuckle(x=0.6199395656585693, y=0.33022454380989075, z=0.33022454380989075),
        Knuckle(x=0.6081591248512268, y=0.23003709316253662, z=0.23003709316253662),
        Knuckle(x=0.6031588912010193, y=0.1476115584373474, z=0.1476115584373474),
        Knuckle(x=0.7093269228935242, y=0.44230031967163086, z=0.44230031967163086),
        Knuckle(x=0.7025118470191956, y=0.2813439965248108, z=0.2813439965248108),
        Knuckle(x=0.7004359364509583, y=0.17170065641403198, z=0.17170065641403198),
        Knuckle(x=0.7011325359344482, y=0.08073118329048157, z=0.08073118329048157),
        Knuckle(x=0.7682938575744629, y=0.45042523741722107, z=0.45042523741722107),
        Knuckle(x=0.7718832492828369, y=0.30062031745910645, z=0.30062031745910645),
        Knuckle(x=0.7744824290275574, y=0.20228365063667297, z=0.20228365063667297),
        Knuckle(x=0.7753350138664246, y=0.11893659830093384, z=0.11893659830093384),
        Knuckle(x=0.8242095708847046, y=0.4851493537425995, z=0.4851493537425995),
        Knuckle(x=0.8444724082946777, y=0.37603092193603516, z=0.37603092193603516),
        Knuckle(x=0.8587654232978821, y=0.3004281520843506, z=0.3004281520843506),
        Knuckle(x=0.8679840564727783, y=0.23021116852760315, z=0.23021116852760315),
    ]
