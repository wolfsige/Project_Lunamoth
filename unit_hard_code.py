def main():

    unit_list = [
        {
            "name": "Lunamoth, the Shadow Huntress",
            "element": "Dark",
            "rarity": "SSR",
            "skills": [
                {
                    "skill": 1,
                    "name": "Shadow Claw",
                    "type": "attack",
                    "target": "enemy",
                    "power": 40,
                    "description": "Lash out at the target, digging your claws into them."
                },
                {
                    "skill": 2,
                    "name": "Temporal Orb",
                    "type": "attack",
                    "power": 75,
                    "cool_down": 3,
                    "effects": [
                        {
                            "type": "debuff",
                            "target": "enemy",
                            "effect": "spd_down",
                            "chance": 50,
                            "duration": 2
                        }
                    ],
                    "description": "Distort the essence of the target and reduce their speed for 2 turns."
                },
                {
                    "skill": 3,
                    "name": "Wither and Bloom",
                    "type": "attack",
                    "power": 150,
                    "cool_down": 5,
                    "effects": [
                        {
                            "type": "debuff",
                            "target": "enemy",
                            "effect": "def_down",
                            "chance": 100,
                            "value": 25,
                            "duration": 2
                        },
                        {
                            "type": "atb_manipulate",
                            "target": "enemy",
                            "effect": "atb_down",
                            "chance": 80,
                            "value": 15
                        },
                        {
                            "type": "atb_manipulate",
                            "target": "self",
                            "effect": "atb_up",
                            "value": 15
                        }
                    ],
                    "description": "Wither the target's life force, dealing damage, breaking their defense, and stealing attack bar."
                }
            ]
        },
        {
            "name": "Mino, the Dawnwarden",
            "element": "Light",
            "rarity": "SSR",
            "skills": [
                {
                    "skill": 1,
                    "name": "Sunbreak Knuckles",
                    "type": "attack",
                    "target": "enemy",
                    "power": 20,
                    "effects": [
                        {
                            "type": "buff",
                            "target": "random_ally",
                            "effect": "atk_up",
                            "chance": 15,
                            "duration": 1
                        },
                        {
                            "type": "buff",
                            "target": "random_ally",
                            "effect": "regen",
                            "chance": 25,
                            "duration": 1
                        }
                    ],
                    "description": "Strike with radiant force, bolstering your and your allies' resolve. Chance to randomly apply ATK Up and Regen."
                },
                {
                    "skill": 2,
                    "name": "Solar Aegis",
                    "type": "buff",
                    "power": 0,
                    "cool_down": 3,
                    "effects": [
                        {
                            "type": "buff",
                            "target": "target_ally",
                            "effect": "def_up",
                            "value": 25,
                            "duration": 2
                        },
                        {
                            "type": "buff",
                            "target": "target_ally",
                            "effect": "regen",
                            "duration": 2
                        }
                    ],
                    "description": "Raise a shield of divine light, protecting allies from harm and blessing their blade. Increase an ally's DEF and grant Regen."
                },
                {
                    "skill": 3,
                    "name": "Radiant Resurgence",
                    "type": "buff",
                    "power": 80,
                    "cool_down": 4,
                    "effects": [
                        {
                            "type": "buff",
                            "target": "all_allies",
                            "effect": "atk_up",
                            "value": 25,
                            "duration": 3
                        },
                        {
                            "type": "atb_manipulate",
                            "target": "all_allies",
                            "effect": "atb_up",
                            "value": 100
                        }
                    ],
                    "description": "Fill your allies with the resolve to move forward and grant them divine radiance. Fill ATB and grant ATK Up."
                }
            ]
        },
        {
            "name": "Skav-009, the Failed Experiment",
            "element": "Dark",
            "rarity": "SR",
            "skills": [
                {
                    "skill": 1,
                    "name": "Shiny Sharp Bite",
                    "type": "attack",
                    "power": 30,
                    "effects": [
                        {
                            "type": "debuff",
                            "target": "enemy",
                            "effect": "dmg_over_time",
                            "chance": 35,
                            "duration": 1
                        },
                        {
                            "type": "debuff",
                            "target": "enemy",
                            "effect": "atk_down",
                            "chance": 15,
                            "duration": 1
                        }
                    ],
                    "description": "Lunges at the target with twitching hunger, biting with cracked warp-crystal teeth. Chance to inflict DOT and ATK Down."
                },
                {
                    "skill": 2,
                    "name": "More Juice, More Power!",
                    "type": "buff",
                    "power": 0,
                    "cool_down": 4,
                    "effects": [
                        {
                            "type": "buff",
                            "target": "self",
                            "effect": "atk_up",
                            "duration": 2
                        },
                        {
                            "type": "buff",
                            "target": "self",
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
                    "description": "Slams a crystal shard into her arm and screams—in pleasure? Gain ATK Up, SPD Up, and DEF Down for 2 turns."
                },
                {
                    "skill": 3,
                    "name": "Raat! Gaat!",
                    "type": "attack",
                    "power": 200,
                    "cool_down": 5,
                    "effects": [
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
                            "chance": 50
                        }
                    ],
                    "description": "Mouth dripping. All you hear is click, click, boom. Deals double damage if DEF Down is active on self. Also has a chance to Stun."
                }
            ]
        },
        {
            "name": "Mistress of Mayhem",
            "element": "Fire",
            "rarity": "SR",
            "skills": [
                {
                    "skill": 1,
                    "name": "Curtain Call",
                    "type": "attack",
                    "target": "enemy",
                    "power": 30,
                    "effects": [
                        {
                            "type": "debuff",
                            "target": "enemy",
                            "effect": "silence",
                            "chance": 30,
                            "duration": 1
                        }
                    ],
                    "description": "Strikes the enemy with a crescendo of sound. Chance to Silence."
                },
                {
                    "skill": 2,
                    "name": "Star of the Show",
                    "type": "debuff",
                    "power": 0,
                    "cool_down": 3,
                    "effects": [
                        {
                            "type": "debuff",
                            "target": "random_enemy",
                            "effect": "taunt",
                            "chance": 60,
                            "duration": 1
                        },
                        {
                            "type": "debuff",
                            "target": "random_enemy",
                            "effect": "atk_down",
                            "chance": 60,
                            "duration": 2
                        }
                    ],
                    "description": "Forces a random enemy to be enthralled with the Mistress. They’ll perform... or die trying."
                },
                {
                    "skill": 3,
                    "name": "Encore",
                    "type": "attack",
                    "power": 100,
                    "cool_down": 5,
                    "effects": [
                        {
                            "if": "target_has_buffs",
                            "modify": "power",
                            "operation": "multiply",
                            "value": 2
                        },
                        {
                            "type": "debuff",
                            "target": "all_enemies",
                            "effect": "def_down",
                            "chance": 80,
                            "value": 25,
                            "duration": 1
                        },
                        {
                            "type": "debuff",
                            "target": "all_enemies",
                            "effect": "stun",
                            "chance": 30,
                            "duration": 1
                        }
                    ],
                    "description": "Unleashes her soul in a final aria, stripping buffs and forcing the spotlight. Deals bonus damage to empowered enemies."
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