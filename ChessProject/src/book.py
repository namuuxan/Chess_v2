from move import Move
from node import Node
from square import Square

class Book:
    
    def __init__(self):
        self.head = Node()
        self._create()

    def next_move(self, game_moves, weighted=True):
        for i, move in enumerate(game_moves):
            if i == 0: node = self.head

            for child in node.children:
                if move == child.value:
                    if len(game_moves)-1 == i:
                        move = child.choose_child(weighted)
                        return move
                    else:
                        node = child

    def _create(self):
        self.head.add_children(
            Node(Move(Square(6, 4), Square(4, 4)), 1365473),
            Node(Move(Square(6, 3), Square(4, 3)), 1050119),
            Node(Move(Square(7, 6), Square(5, 5)), 299548),
            Node(Move(Square(6, 2), Square(4, 2)), 211850),
        )
        
        self.head.children[0].add_children(
            Node(Move(Square(1, 2), Square(3, 2)), 607220),
            Node(Move(Square(1, 4), Square(3, 4)), 296972),
            Node(Move(Square(1, 4), Square(2, 4)), 175686),
            Node(Move(Square(1, 2), Square(2, 2)), 106332),
        )

        self.head.children[1].add_children(
            Node(Move(Square(0, 6), Square(2, 5)), 624094),
            Node(Move(Square(1, 3), Square(3, 3)), 264257),
            Node(Move(Square(1, 4), Square(2, 4)), 47288),
        )

        self.head.children[2].add_children(
            Node(Move(Square(0, 6), Square(2, 5)), 139857),
            Node(Move(Square(1, 3), Square(3, 3)), 79598),
        )

        self.head.children[3].add_children(
            Node(Move(Square(0, 6), Square(2, 5)), 64235),
            Node(Move(Square(1, 4), Square(3, 4)), 45546),
        )

        self.head.children[0].children[0].add_children(
            Node(Move(Square(7, 6), Square(5, 5)), 483773),
            Node(Move(Square(7, 1), Square(5, 2)), 55647),
        )

        self.head.children[0].children[1].add_children(
            Node(Move(Square(7, 6), Square(5, 5)), 262867),
        )

        self.head.children[0].children[2].add_children(
            Node(Move(Square(6, 3), Square(4, 3)), 156673)
        )

        self.head.children[0].children[3].add_children(
            Node(Move(Square(6, 3), Square(4, 3)), 83980)
        )

        self.head.children[1].children[0].add_children(
            Node(Move(Square(6, 2), Square(4, 2)), 430542),
            Node(Move(Square(7, 6), Square(5, 5)), 160061),
        )

        self.head.children[1].children[1].add_children(
            Node(Move(Square(6, 2), Square(4, 2)), 191778),
            Node(Move(Square(7, 6), Square(5, 5)), 78389),
        )

        self.head.children[1].children[2].add_children(
            Node(Move(Square(6, 4), Square(4, 4)), 155950)
        )

        self.head.children[2].children[0].add_children(
            Node(Move(Square(6, 3), Square(4, 3)), 158564),
            Node(Move(Square(6, 2), Square(4, 2)), 89892),
        )

        self.head.children[2].children[1].add_children(
            Node(Move(Square(6, 3), Square(4, 3)), 77741),
            Node(Move(Square(6, 6), Square(5, 6)), 32694),
        )

        self.head.children[3].children[0].add_children(
            Node(Move(Square(6, 3), Square(4, 3)), 417701),
            Node(Move(Square(7, 6), Square(5, 5)), 88843),
        )

        self.head.children[3].children[1].add_children(
            Node(Move(Square(7, 1), Square(5, 2)), 29415),
            Node(Move(Square(6, 6), Square(5, 6)), 15373),
        )

        self.head.children[0].children[0].children[0].add_children(
            Node(Move(Square(1, 3), Square(2, 3)), 196457),
            Node(Move(Square(0, 1), Square(2, 2)), 135043),
            Node(Move(Square(1, 4), Square(2, 4)), 127503),
        )

        self.head.children[0].children[0].children[1].add_children(
            Node(Move(Square(0, 1), Square(2, 2)), 32756),
            Node(Move(Square(1, 4), Square(2, 4)), 8897),
        )

        self.head.children[0].children[1].children[0].add_children(
            Node(Move(Square(0, 1), Square(2, 2)), 226645),
        )

        self.head.children[0].children[2].children[0].add_children(
            Node(Move(Square(1, 3), Square(3, 3)), 153961),
        )

        self.head.children[0].children[3].children[0].add_children(
            Node(Move(Square(1, 3), Square(3, 3)), 80928),
        )

        self.head.children[1].children[0].children[0].add_children(
            Node(Move(Square(1, 4), Square(2, 4)), 211046),
            Node(Move(Square(1, 6), Square(2, 6)), 154877),
            Node(Move(Square(1, 2), Square(3, 2)), 48947),
        )

        self.head.children[1].children[0].children[1].add_children(
            Node(Move(Square(1, 3), Square(3, 3)), 70523),
            Node(Move(Square(1, 6), Square(2, 6)), 65729),
            Node(Move(Square(1, 4), Square(3, 4)), 58615),
        )

        self.head.children[1].children[1].children[0].add_children(
            Node(Move(Square(1, 2), Square(2, 2)), 92378),
            Node(Move(Square(1, 4), Square(2, 4)), 75340),
            Node(Move(Square(3, 3), Square(4, 2)), 23649),
        )

        self.head.children[1].children[1].children[1].add_children(
            Node(Move(Square(0, 6), Square(2, 5)), 69781),
        )

        self.head.children[1].children[2].children[0].add_children(
            Node(Move(Square(1, 3), Square(3, 3)), 153961),
        )

        self.head.children[2].children[0].children[0].add_children(
            Node(Move(Square(1, 3), Square(2, 3)), 196457),
            Node(Move(Square(0, 1), Square(2, 2)), 135043),
            Node(Move(Square(1, 4), Square(2, 4)), 127503),
        )

        self.head.children[2].children[0].children[1].add_children(
            Node(Move(Square(0, 6), Square(2, 5)), 23080),
            Node(Move(Square(0, 1), Square(2, 2)), 13414),
            Node(Move(Square(1, 6), Square(2, 6)), 23080),
        )

        self.head.children[3].children[0].children[0].add_children(
            Node(Move(Square(1, 4), Square(2, 4)), 211046),
            Node(Move(Square(1, 6), Square(2, 6)), 154877),
            Node(Move(Square(1, 2), Square(3, 2)), 48947),
        )

        self.head.children[3].children[0].children[1].add_children(
            Node(Move(Square(1, 6), Square(2, 6)), 33861),
            Node(Move(Square(1, 4), Square(2, 4)), 32507),
            Node(Move(Square(1, 2), Square(3, 2)), 23128),
        )

        self.head.children[3].children[1].children[0].add_children(
            Node(Move(Square(0, 6), Square(2, 5)), 7508),
            Node(Move(Square(0, 1), Square(2, 2)), 4443),
            Node(Move(Square(1, 6), Square(2, 6)), 2706),
        )

        self.head.children[3].children[1].children[1].add_children(
            Node(Move(Square(0, 6), Square(2, 5)), 7988),
            Node(Move(Square(0, 1), Square(2, 2)), 4463),
        )
