# 分析资料契约

order事件含purchase/grant/refund/expire及有效期；call事件含call_id/revision/account/model/service/time/input/output token。重复调用按最新有效修订选取并保留冲突审计。供应商rate按model/unit/valid interval给cost区间和证据，单位不兼容不得换算。收入政策版本显式指定购买时确认、按消耗确认、未用到期确认及退款冲销口径。报告按冻结cohort和service分收入、可映射成本、未映射成本范围及毛利；相邻期间以对称price/volume/mix分解，贡献加总需与可比毛利差额一致；更换政策生成新版本，旧报告保持可复算。
