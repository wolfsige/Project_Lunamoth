def main():

    unit_list = [
        {
            "name" : "Lunamoth, the Shadow Huntress",
            "element" : "Dark",
            "rarity" : "SSR",
            "skills" : [
                {
                    "skill" : 1,
                    "name" : "Shadow Claw",
                    "type" : "attack",
                    "target": "enemy",
                    "power" : 40,
                    "description" : "Lash out at the target, digging you claws into them."
                },
                {
                    "skill" : 2,
                    "name" : "Temporal Orb",
                    "power" : 75,
                    "cool_down": 3,
                    "effects" : [
                        {
                            "type": "debuff",
                            "target": "enemy",
                            "effect": "spd_down",
                            "chance": 50,
                            "duration": 2,
                        }
                    ],
                    "description" : "Distort the essence of the target and reduce their speed for 2 turns."
                },
                {
                    "skill" : 3,
                    "name" : "Wither and Bloom",
                    "power" : 150,
                    "cool_down": 5,
                    "effects" : [
                        {
                            "type" : "debuff",
                            "target" : "enemy",
                            "effect" : "def_down",
                            "chance" : 100,
                            "value" : 25,
                            "duration" : 2
                        },
                        {
                            "type" : "atb_manipulate",
                            "target": "enemy",
                            "effect" : "atb_down",
                            "chance" : 80,
                            "value" : 15
                        },
                        {
                            "type" : "atb_manipulate",
                            "target": "self",
                            "effect" : "atb_up",
                            "value" : 15
                        }
                    ],
                    "description" : "Wither the target's life force dealing damage, "
                                    "breaking their defence, and stealing attack bar."
                }
            ]
        },
        {
            "name": "Mino, the Dawnwarden",
            "element": "Light",
            "rarity": "SSR",
            "skills" : [
                {
                    "skill" : 1,
                    "name" : "Sunbreak Knuckles",
                    "type" : "attack",
                    "target": "enemy",
                    "power" : 20,
                    "effects" : [
                        {
                            "type" : "buff",
                            "target" : "random_ally",
                            "effect" : "atk_up",
                            "chance" : 15,
                            "duration" : 1
                        },
                        {
                            "type": "buff",
                            "target": "random_ally",
                            "effect": "regen",
                            "chance": 25,
                            "duration": 1
                        }
                    ],
                    "description" : "Strike with radiant force, bolstering your and your allies' resolve. "
                                    "Chance to randomly apply atk up and regen"
                },
                {
                    "skill" : 2,
                    "name" : "Solar Aegis",
                    "power" : 0,
                    "cool_down": 3,
                    "effects": [
                        {
                            "type" : "buff",
                            "target" : "tar_ally",
                            "effect" : "def_up",
                            "duration" : 2
                        },
                        {
                            "type" : "buff",
                            "target" : "tar_ally",
                            "effect" : "regen",
                            "duration" : 2
                        }
                    ],
                    "description" : "Raise a shield of divine light, protecting allies from "
                                    "harm and blessing their blade. increase an allies def and grand regen."
                },
                {
                    "skill" : 3,
                    "name" : "Radiant Resurgence",
                    "power" : 80,
                    "cool_down" : 4,
                    "effects" : [
                        {
                            "type" : "buff",
                            "target" : "all_allies",
                            "effect" : "atk_up",
                            "value" : 25,
                            "duration" : 3
                        },
                        {
                            "type" : "atb_manipulate",
                            "target" : "all_allies",
                            "effect" : "atb_up",
                            "value" : 100
                        }
                    ],
                    "description" : "Fill your allies with the resolve to move forward "
                                    "and grant them divine radiance. fill atb and gain atk up"
                }
            ]
        },
        {
            "name": "Skav-009, the Failed Experiment",
            "element": "Dark",
            "rarity": "SR",
            "skills": [
                {
                    "skill" : 1,
                    "name" : "Shiny Sharp Bite",
                    "power" : 30,
                    "effects" : [
                        {
                            "type" : "debuff",
                            "target" : "enemy",
                            "effect" : "dmg_over_time",
                            "chance" : 35,
                            "duration" : 1
                        },
                        {
                            "type" : "debuff",
                            "target" : "enemy",
                            "effect" : "atk_down",
                            "chance" : 15,
                            "duration" : 1
                        }
                    ],
                    "description" : "Lunges at the target with twitching hunger, biting with cracked warp-crystal teeth."
                                    "chance to inflict a DOT and smaller chance to inflict atk down."
                },
                {
                    "skill" : 2,
                    "name" : "More Juice, More Power!",
                    "power" : 0,
                    "cool_down" : 4,
                    "effects" : [
                        {
                            "type": "buff",
                            "target" : "self",
                            "effect" : "atk_up",
                            "duration" : 2
                        },
                        {
                            "type": "buff",
                            "target" : "self",
                            "effect": "spd_up",
                            "duration": 2
                        },
                        {
                            "type": "debuff",
                            "target": "self",
                            "effect": "def_down",
                            "duration": 2
                        }
                    ],
                    "description" : "Slams a crystal shard into her arm and screams, in pleasure? "
                                    "Gain atk up, speed up, and a def down for 2 turns."
                },
                {
                    "skill": 3,
                    "name": "Raat! Gaat!",
                    "power": 200,
                    "cool_down": 5,
                    "effect" : [
                        {
                            "if": "self_has_def_down",
                            "modify": "power",
                            "operation": "multiply",
                            "value": 2
                        },
                        {
                            "type": "debuff",
                            "target": "enemy",
                            "effect": "stun",
                            "duration": 1,
                            "chance" : 50
                        }
                    ],
                    "description" : "Mouth dripping. All you hear is click, click, boom."
                                    "If Skav-009 has a def down applied to her this skill deals double damage."
                                    "Additionally has a chance to stun target."
                }
            ]
        },
        {
            "name" : "Mistress of Mayhem",
            "element": "Fire",
            "rarity": "SR",
            "skills": [
                {

                }
            ]
        },
        {
            "name" : "SR 3"
        },
        {
            "name" : "SR 4"
        },
        {
            "name" : "SR 5"
        },
        {
            "name" : "R 1"
        },
        {
            "name" : "R 2"
        },
        {
            "name" : "R 3"
        },
        {
            "name" : "R 4"
        },
        {
            "name" : "R 5"
        },
        {
            "name" : "R 6"
        },
    ]


main()