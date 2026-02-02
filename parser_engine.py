
def doQuery (column, city="none", operand="none", quantity=0): 
    if city != "none":
        if column == "population":
            doCityPopulationQuery(city)
        elif column == "where":
            doCityWhereQuery(city)
        elif column == "state":
            doCityStateQuery(city)
        elif column == "area":
            doCityAreaQuery(city)
        elif column == "rank":
            doCityRankQuery(city)
        elif column == "big":
            doCityBigQuery(city)
    elif quantity != 0:
        if column == "population":
            doNumPopulationQuery(operand, quantity)
        elif column == "wage":
            doNumWageQuery(operand, quantity)
        elif column == "area":
            doNumAreaQuery(operand, quantity)
        elif column == "rank":
            doNumRankQuery(operand, quantity)
    else:
        Invalid query message