from django.db import models

"""Due to my limited understanding, I couldn't convert 
the variable names from the tutorial video into ones 
that were more appropriate for my program. 

As a solution, I just used the existing and made sure 
to remember what detail corresponds to what variable.
Kindly see the correspondences below."""

class Record(models.Model):
	# Created At -> Recorded At (functions the same way)
	created_at = models.DateTimeField(auto_now_add=True)
	# first_name -> title
	first_name = models.CharField(max_length=50)
	# last_name -> author
	last_name = models.CharField(max_length=50)
	# email -> dream_type
	email = models.CharField(max_length=100)
	# phone -> dreamed_at
	phone = models.CharField(max_length=50)
	# address -> dream_content
	address = models.CharField(max_length=1000)
	# city -> emotions_felt
	city = models.CharField(max_length=500)
	# state -> poss_causes
	state = models.CharField(max_length=1000)
	# zipcode -> takeaways
	zipcode = models.CharField(max_length=1000)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")