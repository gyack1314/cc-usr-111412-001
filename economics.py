"""Token套餐的预付余额、退款与调用归属核算的来源分区接口。"""
def inspect_records(data):
    rows=data.get('orders')
    if not isinstance(rows,list):raise ValueError('业务分区必须为列表')
    if any(not isinstance(row,dict) for row in rows):raise ValueError('业务记录必须为对象')
    return {'section':'orders','records':len(rows),'keys':sorted({k for row in rows for k in row})}
