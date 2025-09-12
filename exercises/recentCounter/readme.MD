#Recent Counter

##Recent Counter is a class that tracks incoming requests from multiple users over time.
The class is initialized with a single value to indicate the ping lookback duration

###Ping
ping method takes in a user and a timestamp in ms, and the method will return the number pings from that user in the past N seconds, based on the ping lookback duration determined at system start. Each ping call is expected to have increasing time stamp

###Get All
The get_all(user) method can be used to return all ping requests from a given user in the current system regardless of timestamp/duration. method will return a list of timestamps

###Complexities
Class has a space complexity O(n) where n is the number of pings

Ping method has O(log n) time  complexity where n is the number of  pings for the given user. This is because ping uses binary search of a sorted list to determine which pings were in the last N seconds

get_all method has O(1) time and space complexity as it is looking for a value via a key (string) in a hashmap