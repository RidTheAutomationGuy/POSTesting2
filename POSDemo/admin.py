from django.contrib import admin

from .models2 import Owner , Business , storeMaster , storeInventoryMaster , auth ,BusinessInventoryMaster , EmployeeMaster , EmployeeAuth  , Customer ,Product , TaxMaster ,  OwnerDetails , SalesRegister , ModeOfPayment , Barcode , TransactionDetails , SalesPending , GenBill

'''
admin.site.register(ProductInventoryManagement)
admin.site.register(Day_Wise_Employee_Management)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Categories)
admin.site.register(SubCategory)
admin.site.register(Employee)
admin.site.register(Item_Return_Management)
admin.site.register(Wastage)
'''
admin.site.register(Owner)
admin.site.register(OwnerDetails)
admin.site.register(Business)
admin.site.register(BusinessInventoryMaster)
admin.site.register(storeMaster)
admin.site.register(storeInventoryMaster)
admin.site.register(auth)
admin.site.register(EmployeeMaster)
admin.site.register(EmployeeAuth)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(TaxMaster)
admin.site.register(SalesRegister)
admin.site.register(ModeOfPayment)
admin.site.register(Barcode)
admin.site.register(TransactionDetails)
admin.site.register(SalesPending)
admin.site.register(GenBill)