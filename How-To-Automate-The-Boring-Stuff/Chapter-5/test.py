# function that check is chess board is in a valid state.

# 1) check if there is one black and white king - DONE
# 2 )check if there are 16 pieces - DONE
# --> check how many times the string b and w appears must be less than 16
# 3) check if there are at most only 8 pawns - DONE
# 4) check if pieces are on valid spaces - DONE
# 5) check if every piece begins with "w" or "b" - DONE
# followed by "pawn" "knight" "bishop" "rook" "queen" or "king" - DONE

# TODO: IMPROVE CODE TO USE LESS LINES


def isValidChessBoard(Board):
    piecesBlack = ["bpawn", "bknight", "bbishop", "bbrook", "bqueen", "bking"]
    piecesWhite = ["wpawn", "wknight", "wbishop", "wbrook", "wqueen", "wking"]
    Coord = ["1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a",
             "1b", "2b", "3b", "4b", "5b", "6b", "7b", "8b",
             "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c",
             "1d", "2d", "3d", "4d", "5d", "6d", "7d", "8d",
             "1e", "2e", "3e", "4e", "5e", "6e", "7e", "8e",
             "1f", "2f", "3f", "4f", "5f", "6f", "7f", "8f",
             "1g", "2g", "3g", "4g", "5g", "6g", "7g", "8g",
             "1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h"]

    # 1)
    kingBlackCount = 0
    kingWhiteCount = 0

    for value in Board.values():
        if value == "bking":
            kingBlackCount += 1
        if value == "wking":
            kingWhiteCount += 1
        if (kingBlackCount or kingWhiteCount) != 1:
            return False

    # 2)
    piecesBlackCount = 0
    piecesWhiteCount = 0

    for value in Board.values():
        if "b" in value:
            piecesBlackCount += 1
        if "w" in value:
            piecesWhiteCount += 1
        if (piecesBlackCount or piecesBlackCount) > 16:
            return False

    # 3)
    pawnsBlackCount = 0
    pawnsWhiteCount = 0

    for value in Board.values():
        if "bpawn" in value:
            pawnsBlackCount += 1
        if "wpawn" in value:
            pawnsWhiteCount = + 1
        if (pawnsBlackCount or pawnsWhiteCount) > 8:
            return False

    # 4)
    for key in Board.keys():
        if key not in Coord:
            return False

    # 5)

    for value in Board.values():
        if (value not in piecesBlack) and (value not in piecesWhite):
            return False

    return True


theBoard = {"1a": "wking", "1b": "bking"}

print(isValidChessBoard(theBoard))
